import Control.Monad
import Data.Char
import Data.List
import qualified Data.Map.Strict as Map

main :: IO ()
main = do
    nNames <- readLn
    names <- replicateM nNames getLines
    let multipliers = Map.fromList $ zip (sort names) [1..]
    nQueries <- readLn
    replicateM_ nQueries (runQuery multipliers)

getLines :: IO String
getLines = do
    line <- getLine
    return line

score :: String -> Int
score word = foldr (\c t -> ((ord c) - 64) + t) 0 word

runQuery :: Map.Map String Int -> IO ()
runQuery multipliers = do
    word <- getLine
    print ((score word) * (multipliers Map.! word))
