#!/usr/bin/env perl

use strict;

sub outputJobs;

my @crabInput = <STDIN>;
my $workingDir;
my $listOfJobs;
my $getListOfJobs = 0;
print "#!/usr/bin/env bash\n\n";
foreach my $line (@crabInput)
  {
    $line =~ s/\n//g;
    if ($line =~ m/^\tworking directory *[^ ]*$/)
      {
        print outputJobs ($listOfJobs, $workingDir) if $workingDir && $listOfJobs;
        $workingDir = $line;
        $workingDir =~ s/^\tworking directory *([^ ]*)$/$1/;
        $listOfJobs = "";
        $getListOfJobs = 0;
      }
    if ($getListOfJobs && $line =~ m/^.*List of jobs: [^ ]*.*$/)
      {
        $line =~ s/^.*List of jobs: ([^ ]*).*$/$1/;
        $listOfJobs .= "," if $listOfJobs;
        $listOfJobs .= $line;
        $getListOfJobs = 0;
      }
    if ($line =~ m/Jobs with Wrapper Exit Code/)
      {
        $line =~ s/^.*Jobs with Wrapper Exit Code : ([^ ]*).*$/$1/;
        $getListOfJobs = 0;
        $getListOfJobs = 1 if $line != 0 || $line eq "";
      }
    else
      {
        $getListOfJobs = 0;
        $getListOfJobs = 1 if $line =~ m/^.*You can resubmit.*$/;
      }
  }
print outputJobs ($listOfJobs, $workingDir) if $workingDir && $listOfJobs;

sub
outputJobs
{
  my $listOfJobs = shift;
  my $workingDir = shift;

  my $buffer = "";
  my $count = 0;
  my $output = "";
  while ($listOfJobs)
    {
      my $tmpBuffer = $listOfJobs;
      if ($listOfJobs =~ m/^.*,.*$/)
        {
          $tmpBuffer =~ s/^([^,]*),.*$/$1/;
          $listOfJobs =~ s/^[^,]*,(.*)$/$1/;
        }
      else
        {
          $listOfJobs = "";
        }
      my $tmpCount = 1;
      my $first = $tmpBuffer;
      my $last = $tmpBuffer;
      if ($tmpBuffer =~ m/^.*-.*$/)
        {
          $first =~ s/^([^-]*)-[^-]*$/$1/;
          $last =~ s/^[^-]*-([^-]*)$/$1/;
          $tmpCount = $last - $first + 1;
        }
      if ($count + $tmpCount < 500)
        {
          $count += $tmpCount;
          $buffer .= "," if $buffer;
          $buffer .= $tmpBuffer;
        }
      elsif ($count + $tmpCount == 500)
        {
          $buffer .= "," if $buffer;
          $buffer .= $tmpBuffer;
          $output .= "crab -forceResubmit $buffer -c $workingDir\n";
          $buffer = "";
          $count = 0;
        }
      elsif ($count + $tmpCount > 500)
        {
          my $newLast = $first + $count + $tmpCount - 498;
          my $newFirst = $first + $count + $tmpCount - 499;
          $buffer .= "," if $buffer;
          $buffer .= $first . "-" . $newLast;
          $output .= "crab -forceResubmit $buffer -c $workingDir\n";
          $listOfJobs = $newFirst . "-" . $last . "," . $listOfJobs if $listOfJobs;
          $listOfJobs = $newFirst . "-" . $last if !$listOfJobs;
          $buffer = "";
          $count = 0;
        }
    }
  $output .= "crab -forceResubmit $buffer -c $workingDir\n" if $count;
  $output =~ s/-c/-GRID.ce_white_list= -c/g;    # Added by HWW to remove white-listing  

  return $output;
}
