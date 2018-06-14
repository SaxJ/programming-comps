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
                rawLines <- replicateM nLines getLine
                print $ getMax nLines $ map lineToList rawLines

neigh n = (n,n+1)

getMax :: Int -> [[Int]] -> Int
getMax nLines xs = walk 0 0 0 xs
    where
        walk total row col = walk (total + (xs !! row !! col)) 
