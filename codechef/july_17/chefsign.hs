findRange :: String -> Integer -> Integer
findRange (h:tl) cnt
  | h == '<' || h == '>' = 

parseLine :: String -> Integer
parseLine line = findRange line 1

process t
    | t < 1 = return ()
    | otherwise = do
        line <- getLine
        putStrLn $ id $ parseLine line
        process (t-1)


main :: IO ()
main = do
    t <- readLn
    process t
