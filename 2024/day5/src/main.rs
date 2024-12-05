use std::fs;
use std::env;

fn read_file(path: String) -> String {
    let content = fs::read_to_string(path);
    match content {
        Ok(content) => content,
        Err(_) => String::from("Error reading file"),
    }
}

fn correctly_ordered(content: &String) -> i32 {
    let mut rules: Vec<Vec<i32>> = Vec::new();
    let mut pages: Vec<Vec<i32>> = Vec::new();
    let mut lines_iter = content.lines().peekable();
    let mut result = 0;
    while !lines_iter.peek().unwrap().is_empty() {
        let line = lines_iter.next().unwrap();
        let rule: Vec<i32> = line.split("|").map(|x| x.parse().unwrap()).collect();
        rules.push(rule);
    }
    lines_iter.next();
    while lines_iter.peek().is_some() {
        let line = lines_iter.next().unwrap();
        let page: Vec<i32> = line.split(",").map(|x| x.parse().unwrap()).collect();
        pages.push(page);
    }
    for page in pages {
        let mut is_correct = true;
        for rule in rules.iter() {
            if rule.iter().all(|x| page.contains(x)) && page.iter().position(|x| x == &rule[0]).unwrap() > page.iter().position(|x| x == &rule[1]).unwrap() {
                is_correct = false;
                break;
            }
        }
        if is_correct {
            result += page[page.len() / 2];
        }
    }
    result
}

fn updated_incorrects(content: &String) -> i32 {
    let mut rules: Vec<Vec<i32>> = Vec::new();
    let mut pages: Vec<Vec<i32>> = Vec::new();
    let mut lines_iter = content.lines().peekable();
    let mut result = 0;
    while !lines_iter.peek().unwrap().is_empty() {
        let line = lines_iter.next().unwrap();
        let rule: Vec<i32> = line.split("|").map(|x| x.parse().unwrap()).collect();
        rules.push(rule);
    }
    lines_iter.next();
    while lines_iter.peek().is_some() {
        let line = lines_iter.next().unwrap();
        let page: Vec<i32> = line.split(",").map(|x| x.parse().unwrap()).collect();
        pages.push(page);
    }
    for mut page in pages {
        let mut is_correct = true;
        let mut i = 0;
        while i < rules.len() {
            if page.contains(&rules[i][0]) && page.contains(&rules[i][1]) {
                let a = page.iter().position(|x| x == &rules[i][0]).unwrap();
                let b = page.iter().position(|x| x == &rules[i][1]).unwrap();
                if a > b {
                    is_correct = false;
                    page.swap(a, b);
                    i = 0;
                    continue;
                }
            }
            i += 1;
        }
        if !is_correct {
            result += page[page.len() / 2];
        }
    }
    result
}


fn main() {
    let args: Vec<String> = env::args().collect();
    if args.len() < 2 {
        println!("Usage: {} <file>", args[0]);
        return;
    }
    let path = &args[1];
    let content = read_file(path.to_string());
    println!("First part - {}", correctly_ordered(&content));
    println!("Second part - {}", updated_incorrects(&content));
}
