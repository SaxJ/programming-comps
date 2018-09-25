import Control.Monad
import Data.List
import qualified Data.Map.Strict as Map

main :: IO ()
main = do
    print amicables

divisorSums :: Map.Map Int Int
divisorSums =  Map.fromList $ map (\x -> (x, sum $ divisors x)) [1..200000]

amicablePairs = [(a, b) | a <- [1..200000],
                          let b = divisorSums Map.! a,
                          b <= 200000 && divisorSums Map.! b == a && b < a]

divisors :: Int -> [Int]
divisors n = 1 : filter ((==0) . rem n) [2 .. n `div` 2]

amicables :: [Int]
amicables = sort $ foldr (\(x,y) t -> x:y:t) [] amicablePairs 
