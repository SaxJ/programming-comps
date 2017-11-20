import Control.Monad

main :: IO ()
main = loop where
    loop = do
        ln <- getLine
        unless (ln == "42") $ putStrLn ln
        unless (ln == "42") loop

