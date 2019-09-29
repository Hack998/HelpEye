; ModuleID = "/home/samuel/Escritorio/Compi/Prueba/gcc/gen6.py"
target triple = "x86_64-unknown-linux-gnu"
target datalayout = ""

define void @"main"() 
{
entry:
  %".2" = bitcast [7 x i8]* @"rt" to i8*
  %".3" = call i32 (i8*, ...) @"printf"(i8* %".2", i8 12)
  %".4" = bitcast [7 x i8]* @"rrt" to i8*
  %".5" = call i32 (i8*, ...) @"printf"(i8* %".4", i8 13)
  %".6" = bitcast [7 x i8]* @"rrrt" to i8*
  %".7" = call i32 (i8*, ...) @"printf"(i8* %".6", i8 14)
  %".8" = bitcast [10 x i8]* @"rrrrts" to i8*
  %".9" = call i32 (i8*, ...) @"printf"(i8* %".8", i8 15)
  %".10" = bitcast [7 x i8]* @"rrrrrt" to i8*
  %".11" = call i32 (i8*, ...) @"printf"(i8* %".10", i8 16)
  %".12" = bitcast [14 x i8]* @"rrrrrrt" to i8*
  %".13" = call i32 (i8*, ...) @"printf"(i8* %".12", i8 17)
  %".14" = bitcast [10 x i8]* @"rrrrrrrt" to i8*
  %".15" = call i32 (i8*, ...) @"printf"(i8* %".14", i8 18)
  ret void
}

declare i32 @"printf"(i8* %".1", ...) 

@"rt" = internal constant [7 x i8] c"Safe \0a\00"
@"rrt" = internal constant [7 x i8] c"Safe \0a\00"
@"rrrt" = internal constant [7 x i8] c"Safe \0a\00"
@"rrrrts" = internal constant [10 x i8] c"Peligro \0a\00"
@"rrrrrt" = internal constant [7 x i8] c"Safe \0a\00"
@"rrrrrrt" = internal constant [14 x i8] c"Very bright \0a\00"
@"rrrrrrrt" = internal constant [10 x i8] c"Peligro \0a\00"