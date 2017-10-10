import Data.List
import Data.Maybe

readInt :: String -> Int
readInt = read

main :: IO ()
main = do
    cases <- getLine
    loop $ readInt cases
        where
            loop n
              | n > 0 = do
                  line <- getLine
                  print (calculate $ readInt line)
                  loop (n-1)
              | otherwise = return ()

calculate m =
    let
        stepDiff = stepMap $ nearest m - m
        stage = nearest m
     in 
        if even stage then
                      (( ceiling $ fromIntegral m / 2 ) - stepDiff, if even m then m else m-1)
                  else
                      (( ceiling $ fromIntegral m / 2 ), (if even m then m else m-1) - stepDiff)


stepMap :: Int -> Int
stepMap 1 = 1
stepMap 2 = 3
stepMap m = 3 + stepMap (m-2)

steps :: [Int]
steps = [stepMap x | x <- [1..1000]]

nearest :: Int -> Int
nearest n = fromMaybe 0 (findIndex (< n) steps)
