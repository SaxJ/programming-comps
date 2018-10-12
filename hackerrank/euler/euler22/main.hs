import Control.Monad
import Data.Char
import qualified Data.Map.Strict as Map

main :: IO ()
main = do
    nNames <- readLn
    names <- replicateM nNames getLines
    nQueries <- readLn
    replicateM_ nQueries $ runQuery $ makeMap names

getLines :: IO String
getLines = do
    line <- getLine
    return line

makeMap :: [String] -> Map.Map String Int
makeMap names =
    foldr toMap Map.empty names
    where
        score w = 
        toMap mp name = Map.insert name $ score name
