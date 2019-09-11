import Control.Monad

subsequencesOfSize :: Int -> [a] -> [[a]]
subsequencesOfSize n xs = let l = length xs
                          in if n>l then [] else subsequencesBySize xs !! (l-n)
 where
   subsequencesBySize [] = [[[]]]
   subsequencesBySize (x:xs) = let next = subsequencesBySize xs
                             in zipWith (++) ([]:next) (map (map (x:)) next ++ [[]])

calculate :: [Int] -> Int -> Int
calculate nums k = foldr (\v c -> if v == mn then c + 1 else c) 0 sums
    where
        seqs = subsequencesOfSize k nums
        sums = map sum seqs
        mn = minimum sums

process :: IO Int
process = do
    line <- getLine
    let [n, k] = [read x | x <- words line]
    numbersLine <- getLine
    let numbers = [read x | x <- words numbersLine]
    return $ calculate numbers k

main :: IO ()
main = do
    cases <- readLn
    results <- replicateM cases process
    mapM_ (putStrLn . show) results
