-- Enter your code here. Read input from STDIN. Print output to STDOUT
fibs :: [Int]
fibs = 1:1:zipWith (+) fibs (tail fibs)

fibonacci :: Int -> Int
fibonacci n = fibs !! n

getInt :: IO Int
getInt = readLn

maxProduct :: Int -> Int
maxProduct n =
    let
        triplets = [a * b * c | a <- [1..(n `div` 2)], let b = ((n * (2*a - n)) `div` (2 * (a-n))), let c = n - a - b, a^2 + b^2 == c^2]
        mx = if null triplets then -1 else maximum triplets
    in if mx <= 0 then -1 else mx

process :: Int -> IO ()
process t
    | t > 0 = do
        n <- getInt
        putStrLn $ show $ maxProduct n
        process (t-1)
    | otherwise = do
        return ()

main = do
    t <- getInt
    process t
