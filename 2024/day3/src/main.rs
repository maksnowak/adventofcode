use std::fs;
use std::env;
use regex::Regex;

fn read_file(path: String) -> String {
    let content = fs::read_to_string(path);
    match content {
        Ok(content) => content,
        Err(_) => String::from("Error reading file"),
    }
}

fn mul(memory: &String) -> i32 {
    let mut result = 0;
    let re = Regex::new(r"mul\([0-9]+,[0-9]+\)").unwrap();
    for cap in re.captures_iter(&memory) {
        let values = cap[0].strip_prefix("mul(").unwrap().strip_suffix(")").unwrap().split(",").collect::<Vec<&str>>();
        let a = values[0].parse::<i32>().unwrap();
        let b = values[1].parse::<i32>().unwrap();
        result += a * b;
    }
    return result;
}

fn cond_mul(memory: &String) -> i32 {
    let mut result = 0;
    let re = Regex::new(r"mul\([0-9]+,[0-9]+\)").unwrap();
    let mut slices: Vec<&str> = Vec::new();
    let do_slices = memory.split("do()").collect::<Vec<&str>>();
    for slice in do_slices {
        let dont_slices = slice.split("don't()").collect::<Vec<&str>>();
        slices.push(dont_slices[0]);
    }
    let enabled = slices.join("");
    for cap in re.captures_iter(&enabled) {
        let values = cap[0].strip_prefix("mul(").unwrap().strip_suffix(")").unwrap().split(",").collect::<Vec<&str>>();
        let a = values[0].parse::<i32>().unwrap();
        let b = values[1].parse::<i32>().unwrap();
        result += a * b;
    }
    return result;
}

fn main() {
    let args: Vec<String> = env::args().collect();
    let path = &args[1];
    let content = read_file(path.to_string());
    println!("First part - {}", mul(&content));
    println!("Second part - {}", cond_mul(&content));
}
