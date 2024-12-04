use std::fs;
use std::env;

fn read_file(path: String) -> String {
    let content = fs::read_to_string(path);
    match content {
        Ok(content) => content,
        Err(_) => String::from("Error reading file"),
    }
}

fn xmas(array: &Vec<&str>) -> i32 {
    let mut count = 0;
    for i in 0..array.len() {
        for j in 0..array.len() {
            if j + 3 < array.len() && ["XMAS", "SAMX"].contains(&array[i][j..j+4].to_string().as_str()) {
                count += 1;
            }
            if j >= 3 && ["XMAS", "SAMX"].contains(&array[i][j-3..j+1].to_string().as_str()) {
                count += 1;
            }
            if i + 3 < array.len() && ["XMAS", "SAMX"].contains(&array[i..i+4].iter().map(|x| x.chars().nth(j).unwrap()).collect::<String>().as_str()) {
                count += 1;
            }
            if i >= 3 && ["XMAS", "SAMX"].contains(&array[i-3..i+1].iter().map(|x| x.chars().nth(j).unwrap()).collect::<String>().as_str()) {
                count += 1;
            }
            if i >= 3 && j >= 3 {
                let mut substr = String::new();
                for k in 0..4 {
                    substr.push(array[i-k].chars().nth(j-k).unwrap());
                }
                if ["XMAS", "SAMX"].contains(&substr.as_str()) {
                    count += 1;
                }
            }
            if i + 3 < array.len() && j + 3 < array.len() {
                let mut substr = String::new();
                for k in 0..4 {
                    substr.push(array[i+k].chars().nth(j+k).unwrap());
                }
                if ["XMAS", "SAMX"].contains(&substr.as_str()) {
                    count += 1;
                }
            }
            if i >= 3 && j + 3 < array.len() {
                let mut substr = String::new();
                for k in 0..4 {
                    substr.push(array[i-k].chars().nth(j+k).unwrap());
                }
                if ["XMAS", "SAMX"].contains(&substr.as_str()) {
                    count += 1;
                }
            }
            if i + 3 < array.len() && j >= 3 {
                let mut substr = String::new();
                for k in 0..4 {
                    substr.push(array[i+k].chars().nth(j-k).unwrap());
                }
                if ["XMAS", "SAMX"].contains(&substr.as_str()) {
                    count += 1;
                }
            }
        }
    }
    return count / 2; // remove duplicates
}

fn x_mas(array: &Vec<&str>) -> i32 {
    let mut count = 0;
    for i in 0..array.len() {
        for j in 0..array.len() {
            if i + 2 < array.len() && j + 2 < array.len() {
                let mut diag1 = String::new();
                let mut diag2 = String::new();
                for k in 0..3 {
                    diag1.push(array[i+k].chars().nth(j+k).unwrap());
                    diag2.push(array[i+k].chars().nth(j+2-k).unwrap());
                }
                if ["MAS", "SAM"].contains(&diag1.as_str()) && ["MAS", "SAM"].contains(&diag2.as_str()) {
                    count += 1;
                }
            }
        }
    }
    return count;
}

fn main() {
    let args: Vec<String> = env::args().collect();
    if args.len() < 2 {
        println!("Usage: {} <file>", args[0]);
        return;
    }
    let path = &args[1];
    let content = read_file(path.to_string());
    let array = content.split("\n").collect::<Vec<&str>>();
    println!("First part - {}", xmas(&array)); 
    println!("Second part - {}", x_mas(&array));
}
