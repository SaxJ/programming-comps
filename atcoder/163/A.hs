main :: IO ()
main = do
  line <- getLine
  let r = read line
  print $ 2 * pi * r
