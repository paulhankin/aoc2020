import re

def parse_data(f):
	pp = dict()
	for line in f:
		line = line.strip()
		if not line:
			if pp:
				yield pp
			pp = dict()
			continue
		for f in line.split(' '):
			a, b = f.split(':')
			pp[a] = b
	if pp:
		yield pp

valid_fields = 'byr iyr eyr hgt hcl ecl pid'.split()
opt_fields = 'cid'.split()

HGTpat = re.compile(r'(\d+)(cm|in)$')
HCLpat = re.compile(r'#[0-9a-f]{6}$')
ECLpat = re.compile(r'(amb|blu|brn|gry|grn|hzl|oth)$')
PIDpat = re.compile(r'[0-9]{9}$')

def valid(pp):
	try:
		for f in valid_fields:
			if f not in pp:
				return 'missing field %s' % f
			if f == 'byr':
				if not (1920 <= int(pp[f]) <= 2002):
					return 'byr out of range'
			elif f == 'iyr':
				if not (2010 <= int(pp[f]) <= 2020):
					return 'iyr out of range'
			elif f == 'eyr':
				if not (2020 <= int(pp[f]) <= 2030):
					return 'eyr out of range'
			elif f == 'hgt':
				m = HGTpat.match(pp[f])
				if m is None: return False
				if m.group(2) == 'cm':
					if not (150 <= int(m.group(1)) <= 193):
						return 'hgt(cm) out of range'
				else:
					assert m.group(2) == 'in'
					if not (59 <= int(m.group(1)) <= 76):
						return 'hgt(in) out of range'
			elif f == 'hcl':
				if not HCLpat.match(pp[f]):
					return 'hct format'
			elif f == 'ecl':
				if not ECLpat.match(pp[f]):
					return 'ecl format'
			elif f == 'pid':
				if not PIDpat.match(pp[f]):
					return 'pid format'
		return True
	except ValueError:
		return 'exception'

invalid_data = r'''
eyr:1972 cid:100
hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926

iyr:2019
hcl:#602927 eyr:1967 hgt:170cm
ecl:grn pid:012533040 byr:1946

hcl:dab227 iyr:2012
ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277

hgt:59cm ecl:zzz
eyr:2038 hcl:74454a iyr:2023
pid:3556412378 byr:2007
'''

valid_data = '''
pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980
hcl:#623a2f

eyr:2029 ecl:blu cid:129 byr:1989
iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm

hcl:#888785
hgt:164cm byr:2001 iyr:2015 cid:88
pid:545766238 ecl:hzl
eyr:2022

iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719
'''
invalid_passports = list(parse_data(invalid_data.split('\n')))
valid_passports = list(parse_data(valid_data.split('\n')))
for pp in invalid_passports:
	if valid(pp) is True:
		print('want invalid %s, got valid' % pp)
		assert False

for pp in valid_passports:
	if valid(pp) is not True:
		print('want valid %s, got %s' % (pp, valid(pp)))
		assert False

assert len(invalid_passports) == 4
assert len(valid_passports) == 4


def part1():
	T = 0
	with open('day04.txt') as ff:
		for pp in parse_data(ff):
			VF = sum(f in pp for f in valid_fields)
			OF = sum(f in pp for f in opt_fields)
			T += (VF == 7)
			if VF + OF != len(pp):
				print(pp)
				assert False
	return T

def part2():
	T = 0
	with open('day04.txt') as ff:
		for pp in parse_data(ff):
			VF = sum(f in pp for f in valid_fields)
			OF = sum(f in pp for f in opt_fields)
			if VF + OF != len(pp):
				print(pp)
				assert False
			if valid(pp) is True:
				print(pp)
			else:
				print('invalid (%s): %s' % (valid(pp), pp))
			T += valid(pp) is True
	return T


for i, f in enumerate([part1, part2]):
	print('part', i+1, f())

