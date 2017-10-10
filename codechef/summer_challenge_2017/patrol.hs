import Data.Fixed

readInt :: String -> Integer
readInt = read

process :: String -> IO ()
process line = loop $ readInt line
    where
        loop n
          | n > 0 = do
              linez <- getLine
              print (calculate linez)
              loop (n-1)
          | otherwise = return ()

main :: IO ()
main = do
    line <- getLine
    process line

calculate line =
    let [u, v, x] = [read x | x <- words line]
     in x / (u + v)
