require 'chunky_png'

def convolution(img, kernel)
  kernel_size = kernel.length
  x_start = kernel_size / 2
  y_start = kernel_size / 2
  matr = Array.new(img.height) { Array.new(img.width) }

  (x_start...img.height - x_start).each do |i|
    (y_start...img.width - y_start).each do |j|
      val = 0
      (-x_start..x_start).each do |k|
        (-y_start..y_start).each do |l|
          val += img[j + l, i + k] * kernel[k + x_start][l + y_start]
        end
      end
      matr[i][j] = val
    end
  end

  matr
end

def get_angle_number(x, y)
  tg = x != 0 ? y.to_f / x : 999

  if x < 0
    if y < 0
      tg > 2.414 ? 0 : tg < 0.414 ? 6 : 7
    else
      tg < -2.414 ? 4 : tg < -0.414 ? 5 : 6
    end
  else
    if y < 0
      tg < -2.414 ? 0 : tg < -0.414 ? 1 : 2
    else
      tg < 0.414 ? 2 : tg < 2.414 ? 3 : 4
    end
  end
end

def gaussian_blur(img, radius)
  kernel_size = radius * 2 + 1
  kernel = Array.new(kernel_size) { Array.new(kernel_size) }
  sigma = radius / 2.0

  sum = 0.0

  (0..kernel_size - 1).each do |i|
    (0..kernel_size - 1).each do |j|
      x = i - radius
      y = j - radius
      kernel[i][j] = Math.exp(-(x * x + y * y) / (2 * sigma * sigma))
      sum += kernel[i][j]
    end
  end

  (0..kernel_size - 1).each do |i|
    (0..kernel_size - 1).each do |j|
      kernel[i][j] /= sum
    end
  end

  result_img = ChunkyPNG::Image.new(img.width, img.height, ChunkyPNG::Color::TRANSPARENT)

  (0..img.height - 1).each do |i|
    (0..img.width - 1).each do |j|
      val = 0.0

      (-radius..radius).each do |k|
        (-radius..radius).each do |l|
          x = j + l
          y = i + k
          x = 0 if x < 0
          y = 0 if y < 0
          x = img.width - 1 if x >= img.width
          y = img.height - 1 if y >= img.height
          val += img[x, y] * kernel[k + radius][l + radius]
        end
      end

      result_img[j, i] = val.round
    end
  end

  result_img
end

def task(path, standard_deviation, kernel_size, bound_path)
  img = ChunkyPNG::Image.from_file(path)
  img_blur_by_chunky = gaussian_blur(img, standard_deviation)

  img_blur_by_chunky.save("_blur_chunky.png")

  gx = [[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]]
  gy = [[-1, -2, -1], [0, 0, 0], [1, 2, 1]]

  img_gx = convolution(img, gx)
  img_gy = convolution(img, gy)

  matr_gradient = Array.new(img.height) { Array.new(img.width) }

  img.height.times do |i|
    img.width.times do |j|
      matr_gradient[i][j] = img[j, i]
    end
  end

  img.height.times do |i|
    img.width.times do |j|
      matr_gradient[i][j] = Math.sqrt(img_gx[i][j] ** 2 + img_gy[i][j] ** 2)
    end
  end

  img_angles = ChunkyPNG::Image.new(img.width, img.height)

  img.height.times do |i|
    img.width.times do |j|
      img_angles[j, i] = get_angle_number(img_gx[i][j], img_gy[i][j]) * 255 / 7
    end
  end

  img_angles.save("_angles.png")

  max_gradient = matr_gradient.flatten.compact.max
  img_gradient_to_print = ChunkyPNG::Image.new(img.width, img.height)

  img.height.times do |i|
    img.width.times do |j|
      img_gradient_to_print[j, i] = (matr_gradient[i][j] * 255 / max_gradient).to_i
    end
  end

  img_gradient_to_print.save("_gradient.png")

  img_border_not_filtered = ChunkyPNG::Image.new(img.width, img.height)

  img.height.times do |i|
    img.width.times do |j|
      angle = img_angles[j, i]
      gradient = matr_gradient[i][j]

      if (i == 0 || i == img.height - 1 || j == 0 || j == img.width - 1)
        img_border_not_filtered[j, i] = ChunkyPNG::Color.rgb(0, 0, 0)
      else
        x_shift = 0
        y_shift = 0

        case angle
        when 0, 4
          x_shift = 0
        when 1, 3
          x_shift = 1
        when 2
          x_shift = 1
          y_shift = 1
        when 5, 7
          x_shift = 1
          y_shift = -1
        when 6
          y_shift = -1
        end

        is_max = gradient >= matr_gradient[i + y_shift][j + x_shift] && gradient >= matr_gradient[i - y_shift][j - x_shift]
        img_border_not_filtered[j, i] = is_max ? ChunkyPNG::Color.rgb(255, 255, 255) : ChunkyPNG::Color.rgb(0, 0, 0)
      end
    end
  end

  img_border_not_filtered.save("border_not_filtered.png")

  lower_bound = max_gradient / bound_path
  upper_bound = max_gradient - max_gradient / bound_path
  img_border_filtered = ChunkyPNG::Image.new(img.width, img.height)

  img.height.times do |i|
    img.width.times do |j|
      gradient = matr_gradient[i][j]

      if img_border_not_filtered[j, i] == ChunkyPNG::Color.rgb(255, 255, 255)
        if gradient >= lower_bound && gradient <= upper_bound
          flag = false
          (-1..1).each do |k|
            (-1..1).each do |l|
              if flag
                break
              end

              if img_border_not_filtered[j + l, i + k] == ChunkyPNG::Color.rgb(255, 255, 255) &&
                matr_gradient[i + k][j + l] >= lower_bound
                flag = true
                break
              end
            end
          end

          img_border_filtered[j, i] = ChunkyPNG::Color.rgb(255, 255, 255) if flag
        elsif gradient > upper_bound
          img_border_filtered[j, i] = ChunkyPNG::Color.rgb(255, 255, 255)
        end
      end
    end
  end

  img_border_filtered.save("border_filtered.png")
end

task('meow2.png', 10, 3, 15)
task('meow2.png', 10, 3, 6)
task('meow2.png', 100, 11, 15)
