import sys

def generate_negative_bed(positive_bed_file, negative_bed_file):
    with open(positive_bed_file, 'r') as positive_file, open(negative_bed_file, 'w') as negative_file:
        previous_end = None
        for line in positive_file:
            fields = line.strip().split('\t')
            chrom, start, end = fields[:3]
            start = int(start)
            end = int(end)

            if previous_end is not None:
                # make sure start position is less than end position
                if previous_end >= start:
                    continue

                # calculate neg coordinates
                negative_start = previous_end + 1
                negative_end = end - 1
                if negative_start < negative_end:
                    negative_file.write(f"{chrom}\t{negative_start}\t{negative_end}\t.\t0\t.\n")

            previous_end = end

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Formatt: python3 script.py positive_bed_file.bed negative_bed_file.bed")
        sys.exit(1)

    positive_bed_file = sys.argv[1]
    negative_bed_file = sys.argv[2]
    generate_negative_bed(positive_bed_file, negative_bed_file)
    print("Negative BED file generated successfully.")

