import torch
P = torch.load(FakeWordGenTensor.pt)

for i in range(15):
  
  out = list()
  out.append('.')
  out.append('.')
  i = 2
  while True:
    p = P[stoi[out[i-2]], stoi[out[i-1]]]
    ix = torch.multinomial(p, num_samples=1, replacement=True, generator=g).item()
    out.append(itos[ix])
    i += 1
    if stoi[out[i-1]] == 0:
      break
  print(''.join(out))
