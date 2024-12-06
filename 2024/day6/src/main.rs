use std::fs;
use std::env;
use std::time;

fn read_file(path: String) -> String {
    let content = fs::read_to_string(path);
    match content {
        Ok(content) => content,
        Err(_) => String::from("Error reading file"),
    }
}

fn part1(content: &String) -> usize {
    let mut map: Vec<Vec<char>> = content.lines().map(|line| line.chars().collect()).collect();
    let mut position: (usize, usize) = (0, 0);
    for i in 0..map.len() {
        for j in 0..map[i].len() {
            if map[i][j].eq(&'^') {
                position = (i, j);
            }
        }
    }
    let x_bounds = 0..map.len();
    let y_bounds = 0..map[0].len();
    let mut direction: (i32, i32) = (-1, 0);
    while x_bounds.contains(&position.0) && y_bounds.contains(&position.1) {
        let next_pos = (position.0 as i32 + direction.0, position.1 as i32 + direction.1);
        if x_bounds.contains(&(next_pos.0 as usize)) && y_bounds.contains(&(next_pos.1 as usize)) {
            let next = map[next_pos.0 as usize][next_pos.1 as usize];
            if next.eq(&'#') {
                direction = (direction.1, -direction.0);
                continue;
            }
        }
        map[position.0][position.1] = 'X';
        position = (next_pos.0 as usize, next_pos.1 as usize);
    }
    let mut count = 0;
    for i in 0..map.len() {
        count += map[i].iter().filter(|&c| c.eq(&'X')).count();
    }
    count
}

fn part2(content: &String) -> usize {
    let map: Vec<Vec<char>> = content.lines().map(|line| line.chars().collect()).collect();
    let mut count = 0;
    for i in 0..map.len() {
        for j in 0..map[i].len() {
            let mut modified_map = map.clone();
            modified_map[i][j] = '#';
            let mut position: (usize, usize) = (0, 0);
            for k in 0..modified_map.len() {
                for l in 0..modified_map[i].len() {
                    if modified_map[k][l].eq(&'^') {
                        position = (k, l);
                        break;
                    }
                }
            }
            let x_bounds = 0..modified_map.len();
            let y_bounds = 0..modified_map[0].len();
            let mut direction: (i32, i32) = (-1, 0);
            let start = time::Instant::now();
            while x_bounds.contains(&position.0) && y_bounds.contains(&position.1) {
                if start.elapsed().as_secs_f32() > 0.1 {
                    count += 1;
                    break;
                }
                let next_pos = (position.0 as i32 + direction.0, position.1 as i32 + direction.1);
                if x_bounds.contains(&(next_pos.0 as usize)) && y_bounds.contains(&(next_pos.1 as usize)) {
                    let next = modified_map[next_pos.0 as usize][next_pos.1 as usize];
                    if next.eq(&'#') {
                        direction = (direction.1, -direction.0);
                        continue;
                    }
                }
                position = (next_pos.0 as usize, next_pos.1 as usize);
            }
        }
    }
    count
}

fn main() {
    let args: Vec<String> = env::args().collect();
    if args.len() < 2 {
        println!("Please provide a file path");
        return;
    }
    let path = &args[1];
    let content = read_file(path.to_string());
    println!("First part - {}", part1(&content));
    println!("Second part - {}", part2(&content));
}
