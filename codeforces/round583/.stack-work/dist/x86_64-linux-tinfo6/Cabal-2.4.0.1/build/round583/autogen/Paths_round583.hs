{-# LANGUAGE CPP #-}
{-# LANGUAGE NoRebindableSyntax #-}
{-# OPTIONS_GHC -fno-warn-missing-import-lists #-}
module Paths_round583 (
    version,
    getBinDir, getLibDir, getDynLibDir, getDataDir, getLibexecDir,
    getDataFileName, getSysconfDir
  ) where

import qualified Control.Exception as Exception
import Data.Version (Version(..))
import System.Environment (getEnv)
import Prelude

#if defined(VERSION_base)

#if MIN_VERSION_base(4,0,0)
catchIO :: IO a -> (Exception.IOException -> IO a) -> IO a
#else
catchIO :: IO a -> (Exception.Exception -> IO a) -> IO a
#endif

#else
catchIO :: IO a -> (Exception.IOException -> IO a) -> IO a
#endif
catchIO = Exception.catch

version :: Version
version = Version [0,1,0,0] []
bindir, libdir, dynlibdir, datadir, libexecdir, sysconfdir :: FilePath

bindir     = "/home/saxonj/Documents/programming-comps/codeforces/round583/.stack-work/install/x86_64-linux-tinfo6/85b0bfb0253eb20f2e8e25bff4afcf29b2daa456d5943a4b0e2f6b971b3ba279/8.6.5/bin"
libdir     = "/home/saxonj/Documents/programming-comps/codeforces/round583/.stack-work/install/x86_64-linux-tinfo6/85b0bfb0253eb20f2e8e25bff4afcf29b2daa456d5943a4b0e2f6b971b3ba279/8.6.5/lib/x86_64-linux-ghc-8.6.5/round583-0.1.0.0-4F2wjXEahZ38MLbTGHek33-round583"
dynlibdir  = "/home/saxonj/Documents/programming-comps/codeforces/round583/.stack-work/install/x86_64-linux-tinfo6/85b0bfb0253eb20f2e8e25bff4afcf29b2daa456d5943a4b0e2f6b971b3ba279/8.6.5/lib/x86_64-linux-ghc-8.6.5"
datadir    = "/home/saxonj/Documents/programming-comps/codeforces/round583/.stack-work/install/x86_64-linux-tinfo6/85b0bfb0253eb20f2e8e25bff4afcf29b2daa456d5943a4b0e2f6b971b3ba279/8.6.5/share/x86_64-linux-ghc-8.6.5/round583-0.1.0.0"
libexecdir = "/home/saxonj/Documents/programming-comps/codeforces/round583/.stack-work/install/x86_64-linux-tinfo6/85b0bfb0253eb20f2e8e25bff4afcf29b2daa456d5943a4b0e2f6b971b3ba279/8.6.5/libexec/x86_64-linux-ghc-8.6.5/round583-0.1.0.0"
sysconfdir = "/home/saxonj/Documents/programming-comps/codeforces/round583/.stack-work/install/x86_64-linux-tinfo6/85b0bfb0253eb20f2e8e25bff4afcf29b2daa456d5943a4b0e2f6b971b3ba279/8.6.5/etc"

getBinDir, getLibDir, getDynLibDir, getDataDir, getLibexecDir, getSysconfDir :: IO FilePath
getBinDir = catchIO (getEnv "round583_bindir") (\_ -> return bindir)
getLibDir = catchIO (getEnv "round583_libdir") (\_ -> return libdir)
getDynLibDir = catchIO (getEnv "round583_dynlibdir") (\_ -> return dynlibdir)
getDataDir = catchIO (getEnv "round583_datadir") (\_ -> return datadir)
getLibexecDir = catchIO (getEnv "round583_libexecdir") (\_ -> return libexecdir)
getSysconfDir = catchIO (getEnv "round583_sysconfdir") (\_ -> return sysconfdir)

getDataFileName :: FilePath -> IO FilePath
getDataFileName name = do
  dir <- getDataDir
  return (dir ++ "/" ++ name)
