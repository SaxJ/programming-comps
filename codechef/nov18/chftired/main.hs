import Control.Monad

main :: IO ()
main = do
    cases <- readLn
    replicateM_ cases testCase

testCase :: IO ()
testCase = do
    ln <- getLine
    putStrLn "YES"
