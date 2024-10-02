use std::io::{self, BufRead, Write};

fn can_reach(reaches: &Vec<usize>, n: usize, cur: &mut Vec<usize>) -> bool {
  if cur.len() == n {
    return cur.iter().map(|&x| reaches[x - 1]).fold(0, |acc, x| acc | x) == 15;
  }

  let mut valid = (1 ..= reaches.len()).collect::<Vec<usize>>();
  valid.retain(|&x| !cur.contains(&x));

  for x in valid {
    cur.push(x);
    if can_reach(reaches, n, cur) {
      return true;
    }
    cur.pop();
  }

  return false;
}

fn main() {
  let stdin = io::stdin();
  let stdout = io::stdout();

  let mut reader = stdin.lock().lines();
  let mut writer = io::BufWriter::new(stdout.lock());

  let line = reader.next().unwrap().unwrap();
  let mut parts = line.split_whitespace();

  let (l, w, n, r) = (
    parts.next().unwrap().parse::<usize>().unwrap(),
    parts.next().unwrap().parse::<usize>().unwrap(),
    parts.next().unwrap().parse::<usize>().unwrap(),
    parts.next().unwrap().parse::<usize>().unwrap(),
  );

  let cranes = (0 .. n).map(|_| {
    let line = reader.next().unwrap().unwrap();
    let mut parts = line.split_whitespace();
    (
      parts.next().unwrap().parse::<isize>().unwrap(),
      parts.next().unwrap().parse::<isize>().unwrap(),
    )
  }).collect::<Vec<(isize, isize)>>();


  let centers = [ (-(l as f64 / 2.0), 0.0), (l as f64 / 2.0, 0.0), (0.0, -(w as f64 / 2.0)), (0.0, w as f64 / 2.0) ];
  let mut reachable = [false, false, false, false];

  let reaches = cranes.iter().map(|&(x, y)| {
    let mut reach = 0;
    for (i, &(cx, cy)) in centers.iter().enumerate() {
      if (x as f64 - cx).powf(2.0) + (y as f64 - cy).powf(2.0) <= (r as f64).powf(2.0) {
        reachable[i] = true;
        reach |= 1 << i;
      }
    }
    reach
  }).collect::<Vec<usize>>();

  if reachable.iter().any(|&x| !x) {
    writeln!(writer, "Impossible").unwrap();
    writer.flush().unwrap();
    return;
  }

  for i in 1 ..= std::cmp::min(n, 4) {
    if can_reach(&reaches, i, &mut vec![]) {
      writeln!(writer, "{}", i).unwrap();
      writer.flush().unwrap();
      return;
    }
  }
}
