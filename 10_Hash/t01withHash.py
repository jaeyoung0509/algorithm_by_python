def solution(participant ,completion):
  answer = ''
  temp = 0
  dic = {}
  for p in participant:
      dic[hash(part)] = p
      temp += int(hash(part))
  for c in completion:
      temp -= dic[c]
  answer = dic[temp]
  return answer
