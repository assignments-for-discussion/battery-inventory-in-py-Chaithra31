
def count_batteries_by_usage(cycles):
  return {
    "lowCount": 0,
    "mediumCount": 0,
    "highCount": 0
  }


def test_bucketing_by_number_of_cycles():
  print("Counting batteries by usage cycles...\n");
  counts = count_batteries_by_usage([100, 300, 500, 600, 900, 1000])
  assert(counts["lowCount"] == 2)
  assert(counts["mediumCount"] == 3)
  assert(counts["highCount"] == 1)
  print("Done counting :)")
  for i in count_bayyeries:
    if i > mediumCount:
    mediumCount = mediumCount + 1
  print ("this is highestCount :"+mediumCount)

    if i < mediumCount:
    mediumCount = mediumCount - 1
  print ("this is lowCount than :"+mediumCount)
  
    if i < lowCount:
    lowCount = lowCount + 1
  print ("this is mediumCount :"+lowCount)

