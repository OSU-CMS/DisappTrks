#!/usr/bin/env perl

use strict;

sub outputJobs;

my @crabInput = <STDIN>;
my $workingDir;
my $listOfJobs;
my $inJobList = 0;
my $output;
print "#!/usr/bin/env bash\n\n";
foreach my $line (@crabInput)
  {
    $line =~ s/\n//g;
    if ($line =~ m/^\tworking directory *[^ ]*$/)
      {
        $output .= outputJobs ($listOfJobs, $workingDir) if $workingDir && $listOfJobs;
        $workingDir = $line;
        $workingDir =~ s/^\tworking directory *([^ ]*)$/$1/;
        $listOfJobs = "";
      }
    if ($inJobList && $line =~ m/^[^ ]*  *[^ ]*  *[^ ]*  *[^ ]* .*$/)
      {
        my $status = $line;
        $status =~ s/^[^ ]*  *[^ ]*  *([^ ]*)  *[^ ]* .*$/$1/;
        $line =~ s/^([^ ]*)  *[^ ]*  *[^ ]*  *[^ ]* .*$/$1/;
        if ($status eq "Created" || $status eq "Submitting" || $status eq "Cancelled")
          {
            $listOfJobs .= "," if $listOfJobs;
            $listOfJobs .= $line;
          }
      }
    if ($line =~ m/ID    END STATUS            ACTION       ExeExitCode JobExitCode E_HOST/)
      {
        $inJobList = 1;
      }
    if ($line =~ m/Total Jobs/ || $line =~ m/ExitCodes Summary/)
      {
        $inJobList = 0;
      }
  }
$output .= outputJobs ($listOfJobs, $workingDir) if $workingDir && $listOfJobs;
print $output . "sleep 60\n";
$output =~ s/kill/forceResubmit/g;
print $output;

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
          $output .= "crab -kill $buffer -c $workingDir\n";
          $buffer = "";
          $count = 0;
        }
      elsif ($count + $tmpCount > 500)
        {
          my $newLast = $first + $count + $tmpCount - 498;
          my $newFirst = $first + $count + $tmpCount - 499;
          $buffer .= "," if $buffer;
          $buffer .= $first . "-" . $newLast;
          $output .= "crab -kill $buffer -c $workingDir\n";
          $listOfJobs = $newFirst . "-" . $last . "," . $listOfJobs if $listOfJobs;
          $listOfJobs = $newFirst . "-" . $last if !$listOfJobs;
          $buffer = "";
          $count = 0;
        }
    }
  $output .= "crab -kill $buffer -c $workingDir\n" if $count;

  return $output;
}
