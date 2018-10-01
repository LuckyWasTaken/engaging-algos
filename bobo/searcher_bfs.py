import os

path = os.getcwd() + '/bobo_town'

def find_bobo_path(queue, GREAT_BOBO):
    while(queue):
        path = queue.pop()
        in_dir = os.scandir(path)
        for item in in_dir:
            if (item.name == GREAT_BOBO):
                return path + '/' + GREAT_BOBO
            if (item.is_dir()):
                new_path = path + '/' + item.name
                queue.append(new_path)
    return None

bobo_path = find_bobo_path([path], 'bobo.txt')

if bobo_path == None:
    print('где же этот чертов бобо')
    exit(0)

print(open(bobo_path).read())
print(open(bobo_path).read())
print(bobo_path)