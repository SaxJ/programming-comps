import qualified Data.Char as C

main :: IO ()
main = do
    line <- getLine
    putStrLn $ nextLucky line

readInt :: String -> Integer
readInt = read

sumFirst line = sum $ map C.ord (take 3 line)

sumSecond line = sum $ map C.ord (drop 3 line)

nextLucky :: String -> String
nextLucky line =
    loop $ readInt line + 1
        where
            loop n = if isLucky n then show n else loop (n + 1)

isLucky :: Integer -> Bool
isLucky n =
    sumFirst line == sumSecond line
    where
        line = show n
