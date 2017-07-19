import Data.Bits
import Data.Word
import Data.Maybe
import Data.List hiding (maximumBy,foldl1')
import Data.Char
import Data.Ord
import Data.Foldable hiding (sum)


foldl1' f l = foldl' f (head l) (tail l)

maximumBy' f = foldl1' max'
  where max' x y = case f x y of
                        LT -> y
                        _  -> x

pairs :: [a] -> [b] -> [(a,b)]
pairs xs ys = [(x,y) | x <- xs, y <- ys]

readInt :: String -> Integer
readInt = read

comparitor (a,b) (c,d)
  | a == c && b == d = EQ
  | gcd a b > gcd c d = GT
  | gcd a b < gcd c d = LT
  | gcd a b == gcd c d && (a+b) > (c+d) = GT
  | gcd a b == gcd c d && (a+b) < (c+d) = LT
  | otherwise = EQ

addTuple :: (Integer, Integer) -> Integer
addTuple (a,b) = a + b

getMax :: String -> String -> Integer
getMax as bs = addTuple $ maximumBy' comparitor $ pairs xs ys
    where
        xs = map readInt $ words as
        ys = map readInt $ words bs

main :: IO ()
main = do
    count <- getLine
    lineA <- getLine
    lineB <- getLine
    print $ getMax lineA lineB
