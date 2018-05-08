import Data.Bits

main :: IO ()
main = do
        cases <- readLn
        runCases cases

runCases :: Int -> IO ()
runCases cases
    | cases > 0 = do
        listSize <- readLn
        line <- getLine
        let sequence = [read x :: Int | x <- words line]
        print $ processSequence listSize sequence
    | otherwise = do return ()

processSequence :: Int -> [Int] -> Int
processSequence size lst =
        let hd:lstB = [a + b | a <- lst, b <- lst] in
            foldr xor hd lstB
