require 'chunky_png'

def blur_fuss
  image = ChunkyPNG::Image.from_file('/Users/kirilltitov/PycharmProjects/multimedia/lr3/output/meow2.png')
  grayscale_image = image.grayscale

  # Размер ядра фильтра и стандартное отклонение
  kernel_size = 5
  standard_deviation = 100

  img_blur1 = gauss_blur(grayscale_image, kernel_size, standard_deviation)
  save_image(img_blur1, 'output/meow2_blur1.png')


  # Другие параметры
  kernel_size = 11
  standard_deviation = 50

  img_blur2 = gauss_blur(grayscale_image, kernel_size, standard_deviation)
  img_blur2.save('output/meow2_blur2.png')

  original_image = grayscale_image.save('output_original.png')
  original_image
end

def gauss_blur(image, kernel_size, standard_deviation)
  kernel = Array.new(kernel_size) { Array.new(kernel_size, 0) }
  a = b = (kernel_size + 1) / 2.0

  # Строим матрицу свёртки
  kernel_size.times do |i|
    kernel_size.times do |j|
      kernel[i][j] = gauss(i, j, standard_deviation, a, b)
    end
  end

  puts kernel.map { |row| row.join(' ') }
  puts '//////////'

  # Нормализуем для сохранения яркости изображения
  sum = kernel.flatten.reduce(:+)
  kernel_size.times do |i|
    kernel_size.times do |j|
      kernel[i][j] /= sum
    end
  end

  puts kernel.map { |row| row.join(' ') }

  # Проходим через внутренние пиксели изображения и выполняем операцию свертки между изображением и ядром
  img_blur = image.clone

  x_start = kernel_size / 2
  y_start = kernel_size / 2
  width = image.width
  height = image.height

  (x_start...(width - x_start)).each do |i|
    (y_start...(height - y_start)).each do |j|
      val_r = val_g = val_b = 0
      (-(kernel_size / 2).to_i..(kernel_size / 2).to_i).each do |k|
        (-(kernel_size / 2).to_i..(kernel_size / 2).to_i).each do |l|
          pixel = image[i + k, j + l]
          val_r += ChunkyPNG::Color.r(pixel) * kernel[k + (kernel_size / 2).to_i][l + (kernel_size / 2).to_i]
          val_g += ChunkyPNG::Color.g(pixel) * kernel[k + (kernel_size / 2).to_i][l + (kernel_size / 2).to_i]
          val_b += ChunkyPNG::Color.b(pixel) * kernel[k + (kernel_size / 2).to_i][l + (kernel_size / 2).to_i]
        end
      end
      img_blur[i, j] = ChunkyPNG::Color.rgb(val_r.round, val_g.round, val_b.round)
    end
  end

  img_blur
end

# Координаты пикселя, станд. отклонение, координаты центра ядра
def gauss(x, y, omega, a, b)
  omega2 = 2 * omega ** 2
  m1 = 1 / (Math::PI * omega2)
  m2 = Math.exp(-((x - a) ** 2 + (y - b) ** 2) / omega2)
  m1 * m2
end

blur_fuss
