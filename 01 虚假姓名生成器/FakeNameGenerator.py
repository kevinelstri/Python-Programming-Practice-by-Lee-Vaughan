'''
    虚假姓名生成器
'''
import sys
import random

print('welcome to the Fake Name Generator:')

first = ('Emma', 'Emily', 'Madison', 'Isabella', 'Ava', 'Sophia', 'Kaitlyn', 'Hannah', 'Hailey', 'Olivia', 'Sarah', 'Abigail', 'Madeline', 'Lily', 'Kaylee', 'Ella', 'Riley', 'Brianna', 'Alyssa', 'Samantha', 'Lauren', 'Mia', 'Alexis', 'Chloe', 'Ashley',
         'Grace', 'Jessica', 'Elizabeth', 'Taylor', 'Makayla', 'Makenzie', 'Anna', 'Zoe', 'Kayla', 'Sydney', 'Megan', 'Natalie', 'Kylie', 'Rachel', 'Avery', 'Katherine', 'Isabel', 'Victoria', 'Morgan', 'Kyra', 'Jasmine', 'Allison', 'Savannah', 'Julia', 'Jordan')
last = ('Alma', 'Alva', 'Amanda', 'Amelia', 'Amy', 'Anastasia', 'Andrea', 'Angela', 'Ann', 'Anna', 'Annabelle', 'Antonia', 'April', 'Arlene', 'Astrid', 'Athena', 'Audrey', 'Aurora', 'Barbara', 'Beatrice', 'Belinda', 'Bella', 'Belle', 'Bernice', 'Bertha', 'Beryl', 'Bess', 'Betsy', 'Betty', 'Beverly', 'Blanche', 'Bblythe', 'Bonnie', 'Bridget', 'Camille', 'Candice', 'Cara', 'Carol', 'Caroline', 'Catherine', 'Cathy', 'Cecilia', 'Celeste', 'Charlotte', 'Cherry', 'Cheryl', 'Chloe', 'Christine', 'Claire', 'Clara', 'Constance', 'Cora', 'Coral', 'Cornelia', 'Crystal', 'Cynthia', 'Daisy', 'Dale', 'Dana', 'Daphne', 'Darlene', 'Dawn', 'Debby', 'Deborah', 'Deirdre', 'Delia', 'Denise', 'Diana', 'Dinah', 'Dolores', 'Dominic', 'Donna', 'Dora', 'Doreen', 'Doris', 'Dorothy', 'Eartha', 'Eden', 'Edith', 'Edwina', 'Eileen', 'Elaine', 'Eleanore', 'Elizabeth', 'Ella', 'Elma', 'Elsa', 'Elsie', 'Elva', 'Elvira', 'Emily', 'Emma', 'Enid', 'Erica', 'Erin', 'Esther', 'Ethel', 'Eudora', 'Eunice', 'Evangeline', 'Eve', 'Evelyn', 'Faithe', 'Fanny', 'Fay', 'Flora', 'Florence', 'Frances', 'Freda', 'Frederica', 'Gabrielle', 'Gail', 'Gemma', 'Genevieve', 'Georgia', 'Geraldine',
        'Gill', 'Gladys', 'Gloria', 'Grace', 'Griselda', 'Gustave', 'Gwendolyn', 'Hannah', 'Harriet', 'Hazel', 'Hedda', 'Hedy', 'Helen', 'Heloise', 'Hermosa', 'Hilda', 'Hilary', 'Honey', 'Hulda', 'Ida', 'Ina', 'Ingrid', 'Irene', 'Iris', 'Irma', 'Isabel', 'Ivy', 'Jacqueline', 'Jamie', 'Jane', 'Janet', 'Janice', 'Jean', 'Jennifer', 'Jenny', 'Jessie', 'Jessica', 'Jill', 'Jo', 'Joan', 'Joanna', 'Joanne', 'Jocelyn', 'Jodie', 'Josephine', 'Joy', 'Joyce', 'Judith', 'Judy', 'Julia', 'Julie', 'Juliet', 'June', 'Kama', 'Karen', 'Katherine', 'Kay', 'Kelly', 'Kimberley', 'Kitty', 'Kristin', 'Laura', 'Laurel', 'Lauren', 'Lee', 'Leila', 'Lena', 'Leona', 'Lesley', 'Letitia', 'Lilith', 'Lillian', 'Linda', 'Lindsay', 'Lisa', 'Liz', 'Lorraine', 'Louise', 'Lucy', 'Lydia', 'Lynn', 'Mabel', 'Madeline', 'Madge', 'Maggie', 'Mamie', 'Mandy', 'Marcia', 'Marguerite', 'Maria', 'Marian', 'Marina', 'Marjorie', 'Martha', 'Martina', 'Mary', 'Maud', 'Maureen', 'Mavis', 'Maxine', 'Mag', 'May', 'Megan', 'Melissa', 'Meroy', 'Merry', 'Michelle', 'Michaelia', 'Mignon', 'Mildred', 'Mirabelle', 'Miranda', 'Miriam', 'Modesty', 'Moira', 'Molly', 'Mona', 'Monica', 'Muriel', 'Myra', 'Myrna')

number = 1
while number < 11:
    firstName = random.choice(first)
    lastName = random.choice(last)
    fullName = firstName + ' ' + lastName
    print(str(number) + ': The Fake Name Generator is ' + fullName)
    number = number + 1


'''
random 详解：
    random.random()：用于生成一个0到1的随机符点数: 0 <= n < 1.0
    random.uniform()：random.uniform(a, b)，用于生成一个指定范围内的随机符点数，两个参数其中一个是上限，一个是下限。如果a > b，则生成的随机数n: b <= n <= a。如果 a <b， 则 a <= n <= b。
    random.randint()：random.randint(a, b)，用于生成一个指定范围内的整数。其中参数a是下限，参数b是上限，生成的随机数n: a <= n <= b。
    random.randrange()：random.randrange([start], stop[, step])，从指定范围内，按指定基数递增的集合中 获取一个随机数。如：random.randrange(10, 100, 2)，结果相当于从[10, 12, 14, 16, ... 96, 98]序列中获取一个随机数。random.randrange(10, 100, 2)在结果上与 random.choice(range(10, 100, 2) 等效。
    random.choice()：random.choice(sequence)。参数sequence表示一个有序类型。这里要说明 一下：sequence在python不是一种特定的类型，而是泛指一系列的类型。list, tuple, 字符串都属于sequence。
    random.shuffle()：random.shuffle(x[, random])，用于将一个列表中的元素打乱。
    random.sample()：random.sample(sequence, k)，从指定序列中随机获取指定长度的片断。sample函数不会修改原有序列。
'''

print('------------------------------------------')
print('随机数1：' + str(random.random()))
print('随机数2：' + str(random.random()))

print('(10,1)范围内随机数1：' + str(random.uniform(10, 1)))
print('(1,10)范围内随机数2：' + str(random.uniform(1, 10)))

print('(11,22)范围内随机数整数1：'+str(random.randint(11, 22)))
print('(23,89)范围内随机数整数2：'+str(random.randint(23, 89)))

print('递增集合中的随机数1：'+ str(random.randrange(10,18,2)))
print('递增集合中的随机数2：'+ str(random.randrange(5,20,4)))

list = [1,2,3,4,5,6,7,8,9,10]
print('乱序列表1：')
random.shuffle(list)
print(list)
print('乱序列表2：')
random.shuffle(list)
print(list)

temp = [1,2,3,4,5,6,7,8,9,10]
slice = random.sample(temp,5)
print('5个样本为：')
print(slice)

