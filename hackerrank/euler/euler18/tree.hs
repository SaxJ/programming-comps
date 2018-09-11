import qualified Data.Map.Strict as Map
import Control.Monad

main :: IO ()
main = do
        cases <- readLn
        replicateM_ cases test
        where
            lineToList line = [read x | x <- words line]
            test = do
                nLines <- readLn
                tree <- replicateM nLines parseTreeRow
                print $ search tree 0

parseTreeRow :: IO [Int]
parseTreeRow = do
    line <- getLine
    return [read x | x <- words line]

search :: [[Int]] -> Int -> Int
search [] _ = 0
search (c:nxt) myIndex = max (myVal + search nxt myIndex) (myVal + search nxt (myIndex+1))
    where
        myVal = c !! myIndex
