import Data.Char (isDigit, digitToInt)
import Data.List (isPrefixOf)

digits1 = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
digits2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

-- Check if the prefix of a string matches one of the digits above. Return (True, length of digit string, digit) if a match is found. Otherwise false
checkDigit s i
    | i == 9 = (False, -1, -1)
    | isPrefixOf d s = (True, length d, digits2 !! i)
    | otherwise = checkDigit s (i+1)
    where
        d = digits1 !! i

findDigits :: String -> [Int]
findDigits xs
    | null xs = []
    | isDigit c = (digitToInt c):(findDigits cs)
    | isMatch = d:(findDigits (drop (l-1) xs))
    | otherwise = findDigits cs
    where
        (isMatch, l, d) = checkDigit xs 0
        (c:cs) = xs

firstLastDigit :: String -> Int
firstLastDigit = (\x -> read ([head x] ++ [last x]) :: Int) . (filter isDigit)

main = do
    contents <- getContents
    let ls = lines contents
        digits = map findDigits ls
        firstLastDigitsSum = map (\x -> 10 * (head x) + (last x)) digits
    print $ sum firstLastDigitsSum