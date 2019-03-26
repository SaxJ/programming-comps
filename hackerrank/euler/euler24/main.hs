import Data.List
import Control.Monad

perms = sort $ permutations "abcdefghijklm"

main :: IO ()
main = do
    cases <- readLn
    replicateM_ cases testCase

testCase :: IO ()
testCase = do
    n <- readLn
    putStrLn $ perms !! n
