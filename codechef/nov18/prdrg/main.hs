import Control.Monad

main :: IO ()
main = do
    input <- getLine
    let tokens = [read x | x <- words input]
    putStrLn $ unwords $ process tokens

process :: [Int] -> [String]
process xs = foldr calc [] $ tail xs
    where
        calc x acc = (unwords ["1", show (2 ^ x)]): acc
