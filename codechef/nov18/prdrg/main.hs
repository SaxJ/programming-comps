import Control.Monad

main :: IO ()
main = do
    input <- getLine
    let tokens = [read x | x <- words input]
    putStrLn $ unwords $ process tokens

process :: [Int] -> [String]
process xs = foldr calc [] $ tail xs
    where
        calc x acc = (unwords [show a, show b]):acc
            where
                (a, b) = pattern x

pattern :: Int -> (Int, Int)
pattern 1 = (1, 2)
pattern 2 = (1, 4)
pattern n = if even n then (a, b * 2) else (b + a, 2 * b)
    where
        (a, b) = pattern (n - 1)
