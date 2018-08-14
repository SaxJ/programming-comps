grid = [row y | y <- [0..]]
  where
    row 0 = repeat 1 :: [Integer]
    row y = 1:[count x y | x <- [1..]]
    count x y = (grid !! y !! (x-1)) + (grid !! (y-1) !! x)

result :: Int -> Int -> Integer
result x y = (grid !! x !! y) `mod` (10^9 + 7)

readNumbers :: String -> [Int]
readNumbers = map read . words

process :: Int -> IO ()
process n
    | n > 0 = do
        ln <- getLine
        let dims = readNumbers ln
        print $ result (head dims) (last dims)
        process (n - 1)
    | otherwise = return ()

readString :: IO (String)
readString = readLn

readInt :: IO (Int)
readInt = readLn

main = do
    cases <- readInt
    process cases
