package org.myorg;

	import java.io.IOException;
	import java.util.*;
	
	import org.apache.hadoop.fs.Path;
	import org.apache.hadoop.conf.*;
	import org.apache.hadoop.io.*;
	import org.apache.hadoop.mapred.*;
	import org.apache.hadoop.util.*;
	
	public class Ranker {
	
        public static class Map extends MapReduceBase implements Mapper<LongWritable, Text, Text, Text> {
            private final static IntWritable one = new IntWritable(1);
            private Text worda = new Text();
	    private Text wordb = new Text();
	    private Text wordc = new Text();
            public void map(LongWritable key, Text value, OutputCollector output, Reporter reporter) throws IOException {
                String line = value.toString();
	        
		String[] lines = line.split("\n");

                for (int i = 0; i < lines.length; i++) {
		    String[] split = lines[i].split("\\s+");
		    worda.set(split[0]);
		    wordb.set(split[1]);
		    wordc.set(lines[i] + "\n");

		    output.collect(worda, wordc);
		    output.collect(wordb, wordc);
		}
            }
        }
	
        public static class Reduce extends MapReduceBase implements Reducer<Text, Text, Text, Text> {
            public void reduce(Text key, Iterator<Text> values, OutputCollector<Text, Text> output, Reporter reporter) throws IOException {
		StringBuilder result = new StringBuilder();
	        ArrayList<String> matches = new ArrayList<String>();
                while (values.hasNext()) {
                    matches.add(values.next().toString());
                }
		
		Collections.sort(matches, new Comparator<String>() {
			public int compare(String a, String b) {
			    int first = Integer.parseInt(a.split("\\s+")[2].replaceAll("[^0-9]",""));
			    int second = Integer.parseInt(b.split("\\s+")[2].replaceAll("[^0-9]",""));

			if (first > second)
			    return 1;
			else if (first < second)
			    return -1;
			else
			    return 0;
			}
		});
		
		if (matches.size() > 5) {
		    for (int i = 0; i < 5; i++) {
			result.append(matches.get(i).replace("\n","") + ", ");
		    }
		} else {
		    for (String s: matches) {
			result.append(s.replace("\n","") + ", ");
		    }
		}

		output.collect(key, new Text(result.toString()));
            }
        }
	
	   public static void main(String[] args) throws Exception {
	     JobConf conf = new JobConf(Ranker.class);
	     conf.setJobName("ranker");
	
	     conf.setOutputKeyClass(Text.class);
	     conf.setOutputValueClass(Text.class);
	
	     conf.setMapperClass(Map.class);
	     conf.setReducerClass(Reduce.class);
	
	     conf.setInputFormat(TextInputFormat.class);
	     conf.setOutputFormat(TextOutputFormat.class);
	
	     FileInputFormat.setInputPaths(conf, new Path(args[0]));
	     FileOutputFormat.setOutputPath(conf, new Path(args[1]));
	
	     JobClient.runJob(conf);
	   }
	}
	
