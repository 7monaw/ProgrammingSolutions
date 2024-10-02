use std::io::{self, BufRead, Write};

fn lucky(div: usize, cur: u128, n: usize) -> usize {
  if div == n + 1 {
    return 1;
  }

  let mut res = 0;

  for i in 0..10 {
    if div == 1 && i == 0 {
      continue;
    }

    let new: u128 = cur * 10 + i;

    if new % div as u128 == 0 {
      res += lucky(div + 1, new, n);
    }
  }

  return res;
}

fn main() {
  let stdin = io::stdin();
  let stdout = io::stdout();

  let mut reader = stdin.lock().lines();
  let mut writer = io::BufWriter::new(stdout.lock());


  let n = reader.next().unwrap().unwrap().parse::<usize>().unwrap();
  let res = lucky(1, 0, n);
  writeln!(writer, "{}", res).unwrap();
}
