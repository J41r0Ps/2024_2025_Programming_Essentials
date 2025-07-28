weight = float(input('input weight in kilogram: '))
length = int(input('Input length in centimeter: '))

BMI = weight / (length / 100) ** 2  # 2x real division

if BMI < 18:
    interpretation = 'underweight'
elif BMI < 25:
    interpretation = 'normal weight'
elif BMI < 27:
    interpretation = 'slightly overweight'
elif BMI < 30:
    interpretation = 'modarate overweight'
elif BMI < 40:
    interpretation = 'obese'
else:
    interpretation = 'sickly obese'

print('A person of', weight, 'kg with a length of', length,
      'cm has a BMI of', BMI)
print('This is', interpretation + '.')