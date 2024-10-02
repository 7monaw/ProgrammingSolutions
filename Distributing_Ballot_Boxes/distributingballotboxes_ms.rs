use std::io::{self, BufRead, Write};

fn main() {
  let stdin = io::stdin();
  let stdout = io::stdout();

  let mut reader = stdin.lock().lines();
  let mut writer = io::BufWriter::new(stdout.lock());

  loop {
    let (n, b) = {
      let line = reader.next().unwrap().unwrap();
      let mut parts = line.split_whitespace();
      (parts.next().unwrap().parse::<isize>().unwrap(), parts.next().unwrap().parse::<isize>().unwrap())
    };

    if (n, b) == (-1, -1) {
      break;
    }

    let populations = (0..n).map(|_| {
      reader.next().unwrap().unwrap().parse::<usize>().unwrap()
    }).collect::<Vec<usize>>();

    let mut lo = 1;
    let mut hi = populations.iter().max().unwrap().clone();

    while lo < hi {
      let mid = (lo + hi) / 2;
      let mut needed = 0;
      for &p in &populations {
        needed += (p + mid - 1) / mid;
      }
      if needed <= b as usize {
        hi = mid;
      } else {
        lo = mid + 1;
      }
    }

    writeln!(writer, "{}", lo).unwrap();
    reader.next();
  }
}
