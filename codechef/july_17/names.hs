import qualified Data.Char as Char

capitalise :: String -> String
capitalise (head:tail) = Char.toUpper head : map Char.toLower tail
capitalise [] = []

shorten :: String -> String
shorten (head:_) = Char.toUpper head : ['.']
shorten [] = []

cleanName :: [String] -> String
cleanName [a,b,c] =
    unwords [shorten a, shorten b, capitalise c]
cleanName [a,b] =
    unwords [shorten a, capitalise b]
cleanName [a] = capitalise a

process t
    | t < 1 = return ()
    | otherwise = do
        name <- getLine
        putStrLn $ id $ cleanName $ words name
        process (t-1)


main :: IO ()
main = do
    t <- readLn
    process t
