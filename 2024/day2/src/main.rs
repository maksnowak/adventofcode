use std::fs;
use std::env;


fn read_file(path: String) -> String {
    let content = fs::read_to_string(path);
    match content {
        Ok(content) => content,
        Err(_) => String::from("Error reading file"),
    }
}

fn is_safe_1(levels: &Vec<i32>) -> bool {
    if levels.is_sorted() && levels.windows(2).all(|w| (w[1] - w[0]).abs() >= 1 && (w[1] - w[0]).abs() <= 3) {
        return true;
    }
    false
}

fn is_safe_2(levels: &Vec<i32>) -> bool {
    if levels.is_sorted() && levels.windows(2).all(|w| (w[1] - w[0]).abs() >= 1 && (w[1] - w[0]).abs() <= 3) {
        return true;
    }
    else {
        for i in 0..levels.len() {
            let mut temp = levels.clone();
            temp.remove(i);
            if temp.is_sorted() && temp.windows(2).all(|w| (w[1] - w[0]).abs() >= 1 && (w[1] - w[0]).abs() <= 3) {
                return true;
            }
        }
    }
    false
}

fn main() {
    let args: Vec<String> = env::args().collect();
    if args.len() < 2 {
        println!("Usage: {} <file>", args[0]);
        return;
    }
    let path = &args[1];
    let content = read_file(path.to_string());
    let mut safe_1: i32 = 0;
    let mut safe_2: i32 = 0;
    for line in content.lines() {
        let levels: Vec<i32> = line.split_whitespace().map(|x| x.parse::<i32>().unwrap()).collect();
        let reversed: Vec<i32> = levels.clone().iter().rev().map(|x| *x).collect();
        if is_safe_1(&levels) || is_safe_1(&reversed) {
            safe_1 += 1;
        }
        if is_safe_2(&levels) || is_safe_2(&reversed) {
            safe_2 += 1;
        }
    }
    println!("First part - safe reports: {}", safe_1);
    println!("Second part - safe reports: {}", safe_2);
}