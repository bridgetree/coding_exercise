def match(pattern, text):
  contains_text = False
  t_index = 0
  p_index = 0
  while t_index < len(text) and not contains_text:
    if pattern[p_index] == text[t_index]:
      p_index += 1
      if p_index == len(pattern):
        contains_text = True
    else:
      if p_index > 0:
        p_index = 0      
    t_index += 1
  return contains_text
