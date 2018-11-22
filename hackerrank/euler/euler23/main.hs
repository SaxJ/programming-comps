import Control.Monad
import qualified Data.Map.Strict as M

divisors n = [x | x <- [1..(n `div` 2)], n `rem` x == 0]

isAbundant n = (sum $ divisors n) > n

isSumOfAbs oldMap lower n = let
    listToAdd = filter isAbundant [lower..n]
    newMap = foldr (\x carr -> M.insert x 1 carr) oldMap listToAdd
    check a = (M.member a newMap) && (M.member (n - a) newMap)
    abundantList = M.keys newMap
    in
        if n > 28123 then (True, oldMap) else (any check abundantList, newMap)

main :: IO ()
main = do
    cases <- readLn
    runTests 0 cases $ M.singleton 12 1
    where
        runTests testNum totalTests mp
            | testNum == totalTests = return ()
            | otherwise = do
                newMap <- processCase mp
                runTests (testNum + 1) totalTests newMap


processCase :: (M.Map Int Int) -> IO (M.Map Int Int)
processCase oldMap = do
    n <- readLn
    let (good, newMap) = isSumOfAbs oldMap (maximum $ M.keys oldMap) n
    if good then putStrLn "YES" else putStrLn "NO"
    return newMap
