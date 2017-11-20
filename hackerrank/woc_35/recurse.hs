import Data.List.Split

toInt :: String -> Int
toInt s = read s :: Int

createGenerator :: Int -> Int -> Int -> Int -> Int
createGenerator m k = gen
    where
        gen i j
            | i == 0 && j == 0 = m
            | i == j = (gen (i-1) (j-1)) + k
            | i > j = (gen (i - 1) j) - 1
            | i < j = (gen i (j-1)) - 1

join vs = unwords [show x | x <- vs]

main :: IO ()
main = do
        line <- getLine
        let [n, m, k] = [toInt x | x <- words line]
        let generator = createGenerator m k
        let values = [generator j i | j <- [0..n-1], i <- [0..n-1]]
        let lines = chunksOf n values
        mapM_ (putStrLn . join) lines
