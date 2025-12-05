import System.IO
import qualified Data.List as List
import Data.Char (digitToInt)
import Data.Maybe (mapMaybe)

processFile :: FilePath -> IO ()
processFile path = do
    contents <- readFile path
    let ls = lines contents
    mapM_ processFile ls

getJoltage1 :: String -> Maybe Int
getJoltage1 line = do
    case line of
        (_:_:_) ->
            let digit = map digitToInt line
                second = tail (List.scanr1 max digit)
                values = [ 10*x + y | (x, y) <- zip digit second ]
            in Just (maximum values)
        _ -> Nothing

sumJoltages1 :: [String] -> Int
sumJoltages1 = sum . mapMaybe getJoltage1

firstPart :: FilePath -> IO ()
firstPart path = do
    contents <- readFile path
    print $ sumJoltages1 (lines contents)


getJoltage2 :: String -> Maybe Int
getJoltage2 line =
    let digits = map digitToInt line
        build :: [Int] -> Int -> [Int]
        build xs need
          | need <= 0 = []
          | length xs < need = []
          | otherwise =
              let maxRangeLen = length xs - need + 1
                  prefix = take maxRangeLen xs
                  m = maximum prefix
                  idx = case List.elemIndex m prefix of
                                   Just i  -> i
                                   Nothing -> 0
              in m : build (drop (idx + 1) xs) (need - 1)
        picked = build digits 12
    in if length picked == 12
         then Just (List.foldl' (\acc d -> acc * 10 + d) 0 picked)
         else Nothing

sumJoltages2 :: [String] -> Int
sumJoltages2 = sum . mapMaybe getJoltage2

secondPart :: FilePath -> IO ()
secondPart path = do
    contents <- readFile path
    print $ sumJoltages2 (lines contents)

main = do
    firstPart "example.txt"
    firstPart "input.txt"
    secondPart "example.txt"
    secondPart "input.txt"
