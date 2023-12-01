import Data.Char (isDigit)

firstLastDigit :: String -> Int
firstLastDigit = (\x -> read ([head x] ++ [last x]) :: Int) . (filter isDigit)

main = do
    contents <- getContents
    let ls = lines contents
    print $ sum $ map firstLastDigit ls