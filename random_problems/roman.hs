import Prelude hiding (last)
import Data.Maybe

symbols :: [(Char, Int)]
symbols = zip "IVXLCDM" [1,5,10,50,100,500,1000]

romanToInt :: String -> Int
romanToInt = fst
                . foldr
                    ((\c (total, last) ->
                        if c >= last then (total + c, c) else (total - c, c))
                        . fromJust . flip lookup symbols)
                    (0,0)

intToRoman :: Int -> String


main :: IO ()
main = putStrLn "Hello"
