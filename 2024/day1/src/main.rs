use std::fs;
use std::env;


fn read_file(path: String) -> String {
    let content = fs::read_to_string(path);
    match content {
        Ok(content) => content,
        Err(_) => String::from("Error reading file"),
    }
}

fn main() {
    let args: Vec<String> = env::args().collect();
    if args.len() < 2 {
        println!("Usage: {} <file>", args[0]);
        return;
    }
    let path = &args[1];
    let content = read_file(path.to_string());
    let mut first_col: Vec<i32> = Vec::new();
    let mut second_col: Vec<i32> = Vec::new();
    for line in content.lines() {
        let cols: Vec<&str> = line.split_whitespace().collect();
        first_col.push(cols[0].parse::<i32>().unwrap());
        second_col.push(cols[1].parse::<i32>().unwrap());
    }
    first_col.sort();
    second_col.sort();
    // first part
    let mut distance: i32 = 0;
    for i in 0..first_col.len() {
        distance += (first_col[i] - second_col[i]).abs();
    }
    println!("First part: {}", distance);
    // second part
    let mut similarity: i32 = 0;
    for i in 0..first_col.len() {
        similarity += first_col[i] * second_col.iter().filter(|&n| *n == first_col[i]).count() as i32;
    }
    println!("Second part: {}", similarity);
}
