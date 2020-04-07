import datetime

def logger_decor(old_foo):
  def new_foo(*args, **kwargs):
    with open('logging_info.txt', 'w') as f:
      f.write(str(datetime.datetime.today())+'\n')
      something = old_foo(*args, **kwargs)
      f.write(f'{old_foo}'+'\n')
      f.write(str(args)+'\n')
      f.write(str(kwargs)+'\n')
      f.write(str(something)+'\n')
    return something
  return new_foo

@logger_decor
def say_hello(name):
  hello = f'Hello, {name}'
  return hello

say_hello('Polly')